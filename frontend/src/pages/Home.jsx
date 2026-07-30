import RequirementForm from "../components/RequirementForm";

function Home() {
  return (
    <div className="container">
      <h1>🤖 Autonomous Software Engineer</h1>

      <p>
        Generate software projects using AI agents powered by LangGraph and
        FastAPI.
      </p>
      <RequirementForm/>
    </div>
  );
}

export default Home;