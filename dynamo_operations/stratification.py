import itertools
import math

import pandas as pd
import random

from matplotlib import pyplot as plt
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper

# Load your dataset (replace 'videos.csv' with your data source)
df = pd.read_csv('../files/items.csv')

# Define categories (e.g., 'emotion' and 'sex')
categories = ['emotion_id', 'sex']

# Get all unique combinations of categories
category_combinations = list(itertools.product(*[df[category].unique() for category in categories]))

# Initialize an empty dictionary to store videos by category combination
category_combination_videos = {combo: [] for combo in category_combinations}

# Categorize videos based on all category combinations
for _, row in df.iterrows():
    category_combo = tuple(row[category] for category in categories)
    category_combination_videos[category_combo].append(row['filename'])

# Initialize an empty list to store the final set of 132 videos for each rater
final_video_set = []


# Stratified sampling within each category combination
for category_combo in category_combinations:
    videos = category_combination_videos[category_combo]
    selected_videos = random.sample(videos, 1)
    final_video_set.extend(selected_videos)

random.shuffle(category_combinations)

emotion_counts = {}
sex_count = {'m': 0, 'f': 0}


# Stratified sampling within each category combination
for category_combo in category_combinations:
    emotion, sex = category_combo

    # Check if we've seen this emotion before
    if emotion not in emotion_counts:
        emotion_counts[emotion] = 0

    # Check if we've already added one entry for this emotion
    if emotion_counts[emotion] < 1:
        if sex_count[sex] < 22:
            videos = category_combination_videos[category_combo]

            videos = [v for v in videos if v not in final_video_set]

            selected_videos = random.sample(videos, 1)
            final_video_set.extend(selected_videos)

            emotion_counts[emotion] += 1
            sex_count[sex] += 1


# Randomize the order of videos within the final set
random.shuffle(final_video_set)

print(len(final_video_set))

selected_rows = df[df['filename'].isin(final_video_set)]

emotion_id_counts = selected_rows["emotion_id"].value_counts()

# Map emotion IDs to actual emotions using your Mapper class
mapped_emotions = emotion_id_counts.index.map(Mapper.get_emotion_from_id)

# Create a histogram plot
plt.figure(figsize=(12, 6))
plt.bar(mapped_emotions, emotion_id_counts.values)

# Customize the plot
plt.xlabel('Emotion')
plt.ylabel('Frequency')
plt.title('Frequency of Emotions')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

plt.tight_layout()

# Show the plot
plt.show()


sex_counts = selected_rows["sex"].value_counts()
print(sex_counts)