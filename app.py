from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
import json


load_dotenv()
client = OpenAI()


def main():
    """
    Streamlit app to convert video descriptions into JSON format using a fine-tuned OpenAI model.

    The app provides a text area for inputting the video description and generates a JSON
    dictionary with the specified structure when the "Generate JSON" button is clicked.

    """
    st.title("Video Description to JSON Converter")

    st.write("Enter your video description below:")

    video_description = st.text_area("Video Description", height=200)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Generate JSON From Fine Tuned Model"):
            with st.spinner("Generating JSON..."):
                response = client.chat.completions.create(
                    model="ft:gpt-3.5-turbo-0125:fast-nuces::9hBgC0oI",
                    messages=[
                        {
                            "role": "system",
                            "content": 'Given a video description, provide the following fields in a JSON dict: "output_format" (string), "duration" (string), "width" (integer), "height" (integer), and "elements" (array of dicts with fields: "type", "track", "time", "duration", "fill_color", "text", "font_family").',
                        },
                        {"role": "user", "content": video_description},
                    ],
                )
                try:
                    json_data = json.loads(response.choices[0].message.content)
                    st.success("JSON generated successfully!")
                    st.json(json_data)
                except json.JSONDecodeError:
                    st.error("Failed to parse JSON. Here is the raw response:")
                    st.text(response.choices[0].message.content)
    with col2:
        if st.button("Generate JSON from Base model"):
            with st.spinner("Generating JSON..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": 'Given a video description, provide the following fields in a JSON dict: "output_format" (string), "duration" (string), "width" (integer), "height" (integer), and "elements" (array of dicts with fields: "type", "track", "time", "duration", "fill_color", "text", "font_family").',
                        },
                        {"role": "user", "content": video_description},
                    ],
                )
                try:
                    json_data = json.loads(response.choices[0].message.content)
                    st.success("JSON generated successfully!")
                    st.json(json_data)
                except json.JSONDecodeError:
                    st.error("Failed to parse JSON. Here is the raw response:")
                    st.text(response.choices[0].message.content)


if __name__ == "__main__":
    main()
