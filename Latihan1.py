# Mengimpor modul yang diperlukan
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

# Menginisialisasi model dengan nama model dan kunci API Anda
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="API_AI_KAMU"
)

# Mendefinisikan fungsi chatbot
def chatbot(Ajukan_caraperintah_input):
    # Mendefinisikan template
    template = """Pertanyaan: {pertanyaan}
    Silakan berikan jawaban langkah demi langkah:
    """
    # Membuat prompt dengan template dan variabel input
    prompt = PromptTemplate(template=template, input_variables=["pertanyaan"])
  
    # Memformat prompt dengan input pengguna
    prompt_terformat = prompt.format(pertanyaan=str(Ajukan_caraperintah_input))
  
    # Mengembalikan konten dari hasil pemanggilan model
    return openai.invoke(prompt_terformat).content


# Membuat antarmuka Gradio dengan fungsi chatbot sebagai fungsi utama
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
# Meluncurkan antarmuka dan membagikannya
demo.launch(share=True)
