import streamlit as st
import pandas as pd
from streamlit import components
from background import BackgroundCSSGenerator
import base64

st.set_page_config(layout="wide")

img1_path = "background.jpg"
img2_path = "Gemini_Generated_Image (2).jpg"
background_generator = BackgroundCSSGenerator(img1_path, img2_path)
page_bg_img = background_generator.generate_background_css()
st.markdown(page_bg_img, unsafe_allow_html=True)


custom_css = """
<style>
body {
    font-family: serif;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
# Title
st.title("🚀 Unveiling Microsoft's Phi-3: Revolutionizing Mobile Language Model Innovation 📱")

# Introduction
st.header("🌟 Unveiling Phi-3: The Next Frontier in Mobile AI")
st.write("Fresh off the press from Microsoft, Phi-3 has just hit the scene, promising to shake up the world of mobile language models (MLMs) and make AI more accessible to everyone. It's a brand new release, and already it's turning heads with its innovative features and impressive performance.")
st.write("So, let's dive right in and take a closer look at what Phi-3 brings to the table. Join us as we uncover its groundbreaking features, explore its exceptional performance, and speculate on the promising potential it holds for the future of AI.")
# Empowering Mobile AI
st.divider()
st.header("📱 Empowering Mobile AI:")
st.write("Phi-3 is more than just pushing the boundaries of AI; it's about making AI accessible to everyone, everywhere. By deploying Phi-3 on mobile devices, Microsoft democratizes AI, empowering users to leverage cutting-edge language models on the go.")
st.write("Whether it's running on Android or iPhones, Phi-3 brings the power of AI to the palm of your hand, transforming how we interact with technology and opening doors to new possibilities.")

st.divider()
# Phi-3: Redefining Mobile AI
st.header("🔥 Phi-3: Redefining Mobile AI:")
st.write('Phi-3 isn\'t just one model—it\'s a whole family designed with precision to meet a variety of user needs. From the sleek Phi-3-Mini to the powerful Phi-3-Medium, Microsoft provides a spectrum of choices tailored to individual requirements.')
st.write('But what truly distinguishes Phi-3 is its cutting-edge training approach. Unlike conventional methods, Phi-3 undergoes an intricately crafted two-phase training regimen, harnessing top-notch datasets to enhance its language comprehension and reasoning capabilities.')

st.divider()
# Training
st.header("🎓 Training:")
st.write('''Now, let's peek behind the curtain and see how Phi-3-Mini gets its smarts. It all starts with the training process, where Phi-3-Mini learns from tons of data to understand and generate human-like text.

First, Microsoft carefully curates a massive dataset from various sources on the internet. They handpick the best-quality content and filter out the noise to ensure Phi-3-Mini learns from the cream of the crop.

But that's not all. Phi-3-Mini also learns from synthetic data generated by larger language models. This synthetic data teaches Phi-3-Mini logical reasoning skills and other niche capabilities, making it a well-rounded AI powerhouse.

The training process is done in two phases. In the first phase, Phi-3-Mini focuses on absorbing knowledge from the curated web data to build its general understanding of language. Then, in the second phase, it incorporates a selective subset of web data along with synthetic data to enhance its reasoning abilities.

By fine-tuning the training data mixture to match Phi-3-Mini's size, Microsoft ensures that the model performs at its best, delivering impressive results from its compact size''')

st.divider()
# Performance Beyond Expectations
st.header("💪 Performance Beyond Expectations:")
st.write("Even though it's compact, Phi-3-Mini proves itself a formidable contender against larger models such as Mixtral 8x7B and GPT-3.5 across diverse benchmarks. It doesn't just meet expectations—it surpasses them, demonstrating remarkable performance and adaptability.")
st.write("Whether it's dominating benchmarks like MMLU or effortlessly tackling real-world challenges on mobile devices, Phi-3 consistently delivers exceptional outcomes that redefine the possibilities of mobile AI.")

st.divider()
# Potential to Surpass Competitors
st.header("🌟 Potential to Surpass Competitors:")
st.write("While Microsoft claims Phi-3's potential to outperform models like Llama-3, the tech community eagerly awaits independent evaluations to validate these assertions. Nonetheless, the anticipation surrounding Phi-3's capabilities underscores its promising future in the MLM arena.")

st.divider()
# Performance Metrics: A Comparative Analysis
st.header("📊 Performance Metrics: A Comparative Analysis:")
df = pd.read_csv('stats.csv', index_col=0)
# st.write(df)C:\Users\jofra\Desktop\llama 3\111111111111.png
col1,col2=st.columns([1,1])
with col1:
 if "show_df" not in st.session_state:
    st.session_state["show_df"] = False
 show_df = st.checkbox("Show DataFrame")
 if show_df:
    st.session_state["show_df"] = True
 else:
    st.session_state["show_df"] = False
 if st.session_state["show_df"]:
    st.write(df)
 else:
    st.image("111111111111.png")
 

with col2:
   st.write("")
   st.write("")
   st.write("")
   st.image('phi31212.jpg')

st.divider()
# MBPP: A Test of Phi-3-Mini's Mettle
st.header("📝 MBPP: A Test of Phi-3-Mini's Mettle:")
st.write("Phi-3-Mini's performance in Multi-Billion Parameter Performance (MBPP) evaluations further solidifies its position as a top contender in the MLM space. Its versatility and adaptability across various tasks underscore its potential to lead the next wave of AI innovation.")

st.divider()
# Phi-3-Mini: Revolutionizing Mobile Language Models
st.header("🌐 Phi-3-Mini: Revolutionizing Mobile Language Models:")
st.write("Phi-3-Mini serves as a testament to Microsoft's commitment to advancing AI accessibility and usability, despite its compact size. Its impressive performance metrics rival established models in the MLM arena, making it a force to be reckoned with.")
st.write("The Phi-3 lineup offers options tailored to diverse user requirements, ensuring that users can choose the model that best suits their specific needs and preferences.")

st.divider()
# Safety First Approach
st.header("🛡️ Safety First Approach:")
st.write("In an age where ethical considerations and responsible AI usage take center stage, Microsoft integrates safety and robustness upgrades into Phi-3. It places user safety at the forefront while maintaining top-notch performance, ensuring the utmost integrity and reliability in every interaction.")

st.divider()

st.header("🚀 Try It Out Yourself:")
st.subheader("Using Ollama (Run On Your Local CPU):")

st.write("1. Install Ollama from their website: [Ollama.com](https://ollama.com/)")
st.write("2. After installation is complete, open PowerShell and run the command `ollama list`. If it is recognized as a command, you are good to go.")

st.write("3. Type the following command to pull Phi3:")
st.code("ollama pull phi3")

st.write("4. Once the pull is complete, run Phi3 using the following command:")
st.code("ollama run phi3")

st.subheader("Alternatively, Try It Out in a Colab Notebook:")
st.write("You can also try out Phi3 in a Colab notebook by following these steps:")
st.write("1. Click on the following link to open the Colab notebook: [Phi3 Colab Notebook](https://colab.research.google.com/drive/1nS9vk69go9GFXyLdUokOi2M0ZRH4yHt9)")
st.write("2. Follow the instructions provided in the notebook to run and experiment with Phi3.")

st.subheader("Other Methods:")
st.write("There are several other ways to run Phi3, including through Hugging Face's Transformers library and other cloud platforms. However, for simply trying it out, the methods mentioned above are more than sufficient.")

st.subheader("BONUS: Simple Chat Application")
st.write("If you installed Phi3 through Ollama, you can run this simple Chat Application to have a conversation with it instead of doing it in cmd prompt. Check the source code below to get started!")
with st.expander("Source Code"):
    st.markdown("""
    ```python
                import streamlit as st 
from langchain.llms import Ollama

st.title("Test Out the Phi-3 Model By Yourself")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.session_state["model"] = 'phi3'

def load_ollama():
    return Ollama()

ollama = load_ollama()

def model_res_generator():
    for message in st.session_state["messages"]:
        yield message

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        output = ollama.generate(
            model=st.session_state["model"],
            prompts=[prompt]
        )
        message = output.generations[0][0].text
        st.markdown(message)
        st.session_state["messages"].append({"role": "assistant", "content": message})

        """)
    
st.divider()
st.header("💭 My Thoughts")
st.write('''
In the fast-paced world of AI development, the rise of small language models (SLMs) has been pretty mind-blowing. Google kicked things off with their Gemma 7B parameter model, followed by the impressive Llama-3 8B parameter model, and the game hasn't been the same since. These models, despite being relatively small in size, have punched way above their weight class, giving the big boys a run for their money.

Now, with Microsoft's Phi-3 stepping into the ring with its 3 billion parameters and still managing to outperform larger models, it's got everyone wondering: are SLMs about to steal the show? Could this be the year where size doesn't matter as much in the AI world? As SLMs keep getting better and showing off what they can do, it's starting to seem like the days of giant models ruling the roost might be numbered. So, what's your take on all this? Are we on the brink of a new era where smaller models reign supreme?''')


# Conclusion: Pioneering the Future of Mobile AI
st.header("🌈 Conclusion: Living in an Era of Endless Innovation!")
st.write("Wow, what a time to be alive! 🌟 We're witnessing the dawn of a new era filled with endless possibilities and groundbreaking innovations in the world of AI.")
st.write("From mobile assistants that understand us better than ever to AI models that fit right in the palm of our hands, it's like living in a sci-fi movie come to life! 🚀")
st.write("And amidst all this excitement, Phi-3 shines as a beacon of hope for open-source devs, offering its gifts freely to fuel our creativity and drive us forward into a future limited only by our imaginations. 🎨")
st.write("So let's raise a toast to this amazing era we're living in – may it continue to inspire, amaze, and empower us all to reach for the stars! 🌌")
st.image("meme.jpg")

# Additional Resources
st.header("🔗 Additional Resources")
st.write("Want to dive deeper into Phi-3? Check out these resources:")

st.subheader("Microsoft News Articles:")
st.markdown("- [The Phi-3: Small Language Models with Big Potential](https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/?ocid=FY24_soc_omc_br_li_Phi3)")
st.markdown("- [Introducing Phi-3: Redefining What's Possible with SLMs](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/)")

st.subheader("Hugging Face Models:")
st.markdown("- [Phi-3 Mini 128K Instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)")
st.markdown("- [Phi-3 Mini 4K Instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)")




