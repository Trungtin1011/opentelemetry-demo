using System.Diagnostics;
using System.Diagnostics.Metrics;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Logging;

using ILoggerFactory factory = LoggerFactory.Create(builder => builder.AddConsole());
ILogger logger = factory.CreateLogger("Service");

// .NET Diagnostics: create the span factory
using var activitySource = new ActivitySource("Examples.Service");

// .NET Diagnostics: create a metric
using var meter = new Meter("Examples.Service", "1.0");
var successCounter = meter.CreateCounter<long>("srv.successes.count", description: "Number of successful responses");

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
var connectionString = Environment.GetEnvironmentVariable("DB_CONNECTION");
app.MapGet("/", Handler);
app.Run();

async Task<string> Handler()
{
    using (var activity = activitySource.StartActivity("SayHello"))
    {
        activity?.SetTag("ID", 1);
        activity?.SetTag("Message", "Hello, World!");
        activity?.SetTag("ThirdOne", new int[] { 1, 2, 3 });

        var waitTime = Random.Shared.NextDouble(); // max 1 second
        await Task.Delay(TimeSpan.FromSeconds(waitTime));

        activity?.SetStatus(ActivityStatusCode.Ok);

        // .NET Diagnostics: update the metric
        successCounter.Add(1);
    }

    try
    {
        logger.LogInformation("Dotnet Server: Attempting to open SQL connection.");
        using var connection = new SqlConnection(connectionString);
        await connection.OpenAsync();

        using var command = new SqlCommand("SELECT 1", connection);
        using var reader = await command.ExecuteReaderAsync();
        logger.LogInformation($"Dotnet Server: Executed SQL command successfully on {DateTimeOffset.UtcNow}");
        return $"Dotnet Server: Executed SQL command successfully on {DateTimeOffset.UtcNow}";
    }

    catch (Exception ex)
    {
        logger.LogError($"Dotnet Server Error: {ex}");
        return $"Dotnet Server Error: {ex}";
    }
}
