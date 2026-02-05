from concurrent.futures import ThreadPoolExecutor

from core.file_utils import list_files
from core.logging_utils import log

from llm.task_classifier import interpret_task
from reader.template_reader import read_template
from pipeline.document_processor import DocumentProcessor

class AgentRunner:
    def __init__(self, models, template_path, output_dir, max_workers=4):
        self.models = models
        self.template = read_template(template_path)
        self.output_dir = output_dir
        self.max_workers = max_workers

    def run(self, documents_dir: str, instruction: str):
    
        while True:
            task = interpret_task(self.models["task"], instruction)
            if not task["should_process"]:
                log("Instruction does not request document processing.")
                instruction = input("Your prompt\n> ")
            else:
                files = list_files(documents_dir)
                log(f"Found {len(files)} files")
        
                processor = DocumentProcessor(self.models, self.template, self.output_dir)
        
                with ThreadPoolExecutor(max_workers=self.max_workers) as ex:
                    futures = [ex.submit(processor.process, f, task["task_description"]) for f in files]
                    for fut in futures:
                        fut.result()
                break
