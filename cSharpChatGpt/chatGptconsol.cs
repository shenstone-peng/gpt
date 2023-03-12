using System;
using System.Net.Http;
using System.Threading.Tasks;

public class Program
{
    public static async Task Main(string[] args)
    {
        var message = "Hello";
        var apiKey = args[0];
        var url = $"https://api.openai.com/v1/engines/davinci-codex/completions?prompt={message}&max_tokens=10&n=1";
        
        using (var client = new HttpClient())
        {
            client.DefaultRequestHeaders.Add("Authorization", $"Bearer {apiKey}");
            var response = await client.GetAsync(url);
            var content = await response.Content.ReadAsStringAsync();
            Console.WriteLine(content);
        }
    }
}