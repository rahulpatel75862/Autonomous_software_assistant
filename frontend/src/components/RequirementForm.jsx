import { useState } from "react";
import api from "../services/api";

function RequirementForm() {
  const [requirement, setRequirement] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!requirement.trim()) {
      alert("Please enter project requirements.");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post("/generate", {
        requirement,
      });

      console.log(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to generate project.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="requirement-card">
      <h2>Project Requirement</h2>

      <textarea
        placeholder="Describe your project..."
        value={requirement}
        onChange={(e) => setRequirement(e.target.value)}
      />

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Project"}
      </button>
    </div>
  );
}

export default RequirementForm;