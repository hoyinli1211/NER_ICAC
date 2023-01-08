import streamlit as st
import pandas as pd
import prodigy

df = pd.read_csv("https://raw.githubusercontent.com/hoyinli1211/NER_ICAC/main/ICACPressReleases.csv")

st.title("Named Entity Annotation Tool")

# Display the text of the press release
text_input = st.text_area("Press Release Text", df.iloc[0]["text"])

# Add buttons for labeling named entities
person_button = st.button("Person")
organization_button = st.button("Organization")
location_button = st.button("Location")

# Save the annotated data
if person_button or organization_button or location_button:
  # Create a Prodigy dataset to store the annotated data
  dataset = prodigy.Dataset("icac_ner")

  # Add the annotated data to the dataset
  prodigy.log_ner(dataset, entities=ner.extract_entities(text_input), text=text_input)

  # Save the dataset
  prodigy.save(dataset)
  st.write("Annotated data saved!")
