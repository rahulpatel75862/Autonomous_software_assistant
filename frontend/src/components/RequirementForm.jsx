import { useState } from "react";
import api from "../services/api";

function RequirementForm() {
  const [requirement, setRequirement] = useState("");
  const [outputPath, setOutputPath] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  const handleGenerate = async () => {
    if (!requirement.trim()) {
      alert("Please enter requirement.");
      return;
    }

    if (!outputPath.trim()) {
      alert("Please enter output path.");
      return;
    }

    try {
      setLoading(true);

      const res = await api.post("/generate", {
        requirement: requirement,
        output_path: outputPath
      });

      setResponse(res.data);
    } catch (err) {
      console.error(err);

      if (err.response) {
        console.log("Status:", err.response.status);
        console.log("Data:", err.response.data);
        console.log("Headers:", err.response.headers);
      } else if (err.request) {
        console.log("No response received:", err.request);
      } else {
        console.log("Error:", err.message);
      }

      alert("Project generation failed");
    }
  };

  return (
    <div>

      <h2>AI Project Generator</h2>

      <textarea
        rows={8}
        placeholder="Enter your project requirement..."
        value={requirement}
        onChange={(e) => setRequirement(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Output Path"
        value={outputPath}
        onChange={(e) => setOutputPath(e.target.value)}
      />

      <br /><br />

      <button
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Project"}
      </button>

      <br /><br />

      {response && (
        <pre>
          {JSON.stringify(response, null, 2)}
        </pre>
      )}

    </div>
  );
}

export default RequirementForm;