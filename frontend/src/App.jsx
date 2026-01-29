import React, { useState } from "react";
import { Terminal, Code2, Shield, Zap, Loader2 } from "lucide-react";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAudit = async () => {
    if (!url) return;

    setLoading(true);
    setResult(null); // Clear previous results
    console.log("Sending to backend:", url);

    try {
      // Connects Python backend
      const response = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ repo_url: url }),
      });

      const data = await response.json();
      console.log("Results from Python:", data);
      setResult(data); // Save  response
    } catch (error) {
      console.error("Error connecting to backend:", error);
      alert("Failed to connect to backend. Is app.py running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-200 p-8 font-sans selection:bg-blue-500 selection:text-white">
      <div className="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-600/20 rounded-full blur-[120px]" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-600/20 rounded-full blur-[120px]" />
      </div>

      <div className="max-w-5xl mx-auto pt-10">
        {/* Hero Header */}
        <header className="text-center mb-16 space-y-6">
          <div className="inline-flex items-center justify-center p-4 bg-slate-900/50 rounded-2xl border border-slate-800 shadow-xl mb-4 backdrop-blur-sm">
            <Code2
              size={64}
              className="text-blue-500 drop-shadow-[0_0_15px_rgba(59,130,246,0.5)]"
            />
          </div>
          <h1 className="text-6xl font-extrabold tracking-tight">
            <span className="bg-gradient-to-r from-blue-400 via-blue-500 to-purple-600 bg-clip-text text-transparent">
              GitSight AI
            </span>
          </h1>
          <p className="text-slate-400 text-xl max-w-2xl mx-auto leading-relaxed">
            The Autonomous DevOps Auditor.
            <span className="block text-slate-500 text-base mt-2">
              Detect bugs, security flaws, and performance issues in seconds.
            </span>
          </p>
        </header>

        {/*  Input Card */}
        <div className="bg-slate-900/40 backdrop-blur-md p-10 rounded-3xl border border-slate-700/50 shadow-2xl relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />

          <div className="flex flex-col md:flex-row gap-4 relative z-10">
            <div className="flex-1 relative">
              <div className="absolute inset-y-0 left-4 flex items-center pointer-events-none">
                <Shield size={20} className="text-slate-500" />
              </div>
              <input
                type="text"
                placeholder="https://github.com/username/repository"
                className="w-full bg-slate-950/80 border border-slate-700 rounded-xl py-5 pl-12 pr-6 text-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all placeholder:text-slate-600"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleAudit()} // Allowsss pressing Enter
              />
            </div>

            <button
              onClick={handleAudit}
              disabled={loading} // Disable button while loading
              className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 text-white px-10 py-5 rounded-xl font-bold text-lg transition-all transform hover:scale-[1.02] active:scale-[0.98] shadow-lg shadow-blue-900/20 flex items-center justify-center gap-3 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? (
                <>
                  <Loader2 size={24} className="animate-spin" />
                  Scanning...
                </>
              ) : (
                <>
                  <Zap size={24} className="fill-current" />
                  Start Audit
                </>
              )}
            </button>
          </div>

          <div className="mt-6 flex items-center justify-center gap-8 text-sm text-slate-500">
            <div className="flex items-center gap-2">
              <div
                className={`w-2 h-2 rounded-full ${loading ? "bg-yellow-500" : "bg-green-500 animate-pulse"}`}
              />
              <span>
                {loading ? "Processing Repository..." : "System Online"}
              </span>
            </div>
            <span>•</span>
            <span>Supports Python, JS, React</span>
            <span>•</span>
            <span>Powered by Gemini 2.5</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
