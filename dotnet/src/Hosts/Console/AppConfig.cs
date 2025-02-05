﻿using Agience.Core;

namespace Agience.Hosts._Console
{
    internal class AppConfig : HostConfig
    {
        public string? OpenAiApiKey { get; set; }
        public string? OpenAIApiUrl { get; set; }
        public string? CustomNtpHost { get; set; }
        public string? WorkspacePath { get; set; }
    }
}
