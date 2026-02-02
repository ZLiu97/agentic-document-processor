from pathlib import Path
from config.settings import MODELS, MAX_WORKERS
from pipeline.agent_runner import AgentRunner

BASE = Path(__file__).parent.parent

DOCUMENTS = BASE / "documents"
TEMPLATE = BASE / "template.md"
OUTPUT = BASE / "output"


def main():
    instruction = input("What would you like me to do?\n> ")

    agent = AgentRunner(
        models=MODELS,
        template_path=str(TEMPLATE),
        output_dir=str(OUTPUT),
        max_workers=MAX_WORKERS,
    )

    agent.run(str(DOCUMENTS), instruction)


if __name__ == "__main__":
    main()
