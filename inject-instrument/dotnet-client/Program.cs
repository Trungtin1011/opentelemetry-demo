using System.Diagnostics;
using System.Diagnostics.Metrics;
using Microsoft.Extensions.Logging;

using ILoggerFactory factory = LoggerFactory.Create(builder => builder.AddConsole());
ILogger logger = factory.CreateLogger("Client");


// .NET Diagnostics: create the span factory
using var activitySource = new ActivitySource("Examples.Client");

// .NET Diagnostics: create a metric
using var meter = new Meter("Examples.Client", "1.0");
var successCounter = meter.CreateCounter<long>("client.successes.count", description: "Number of successful request");

var url = Environment.GetEnvironmentVariable("SERVICE_ENDPOINT");
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", Handler);
app.Run();

async Task<string> Handler()
{
    using var httpClient = new HttpClient();
    using (var activity = activitySource.StartActivity("Init"))
    {
        activity?.SetTag("ID", 0);
        activity?.SetTag("Message", "Client Hello");

        var waitTime = Random.Shared.NextDouble(); // max 1 second
        await Task.Delay(TimeSpan.FromSeconds(waitTime));

        activity?.SetStatus(ActivityStatusCode.Ok);
    }

    logger.LogInformation($"Dotnet Client: Attempting to connect Dotnet Server at {url}");
    try
    {
        var content = await httpClient.GetStringAsync(url);
        logger.LogInformation($"Dotnet Client: Successfully fetched content from {url}: {content}");
        return $"Dotnet Client: Successfully fetched content from {url}: {content}";
    }
    catch (Exception ex)
    {
        logger.LogError($"Dotnet Client Error: {ex}");
        return $"Dotnet Client Error: {ex}";
    }
}
