from vertexai.generative_models import Part
from vertexai.generative_models import GenerativeModel

def summarize_pdf_document():
    # https://storage.googleapis.com/bhagavan-pub-bucket/project.pdf
    
    file_uri = "gs://bhagavan-pub-bucket/project.pdf"
    pdf_file = Part.from_uri(file_uri, mime_type="application/pdf")
    
    prompt = """
    You are a professional document summarization specialist
    Can you summarise the list of activities involved?
    Make sure each activity can be implimented idipedentely
    Integration can be done at later stage
    Can you also title the project with appropriate name
    Along with, can you generate PlantUML diagram for each activity?
    """
    
    model = "gemini-1.5-pro-001"
    contents = [pdf_file, prompt]
    
    multimodal_model = GenerativeModel(model)

    response = multimodal_model.generate_content(contents=contents)
    print(response.text)

    
def main():
    summarize_pdf_document()
    
if __name__ == "__main__":
    main()
    