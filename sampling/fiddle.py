import itertools
import random
import pandas as pd
from matplotlib import pyplot as plt
from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper


def get_opposite_sex(sex):
    if sex == "m":
        return "f"
    elif sex == "f":
        return "m"
    else:
        raise ValueError(f"{sex} is not a valid sex")


def sample(df_):
    categories = df_["emotion_id"].unique()

    # Initialize an empty dictionary to store videos by category combination
    category_videos = {combo: [] for combo in categories}

    # Categorize videos based on all category combinations
    for _, row in df_.iterrows():
        category = row["emotion_id"]
        category_videos[category].append(row['filename'])

    # Initialize an empty list to store the final set of 132 videos for each rater
    ret = []

    # Stratified sampling within each category combination
    for category in categories:
        videos = category_videos[category]

        selected_videos = random.sample(videos, 1)
        ret.extend(selected_videos)

    return ret


def sample_with_sex(df_):
    # Define categories
    categories = ['emotion_id', 'sex']

    # Get all unique combinations of categories
    category_combinations = list(itertools.product(*[df_[category].unique() for category in categories]))

    # Initialize an empty dictionary to store videos by category combination
    category_combination_videos = {combo: [] for combo in category_combinations}

    # Categorize videos based on all category combinations
    for _, row in df_.iterrows():
        category_combo = tuple(row[category] for category in categories)
        category_combination_videos[category_combo].append(row['filename'])

    # Initialize an empty list to store the final set of 132 videos for each rater
    ret = []

    # Stratified sampling within each category combination
    for category_combo in category_combinations:
        videos = category_combination_videos[category_combo]

        if not videos:
            emotion, sex = category_combo
            videos = category_combination_videos[(emotion, get_opposite_sex(sex))]

        selected_videos = random.sample(videos, 1)
        ret.extend(selected_videos)

    random.shuffle(category_combinations)

    return ret


def evaluate(df_, video_set):
    print(f'{len(video_set)=}')

    selected_rows = df_[df_['filename'].isin(video_set)]
    emotion_id_counts = selected_rows["emotion_id"].value_counts()
    print("all emotions occur 3 times:", (emotion_id_counts == 3).all())

    sex_counts = selected_rows["sex"].value_counts()
    print(f'{sex_counts=}')


sampled = []

for i in range(40):
    # Load your dataset (replace 'videos.csv' with your data source)
    df = pd.read_csv('../files/items.csv')

    sampled_with_sex = sample_with_sex(df[~df['filename'].isin(sampled)])
    sampled.extend(sampled_with_sex)

    sampled_without_sex = sample(df[~df['filename'].isin(sampled)])
    sampled.extend(sampled_without_sex)

    sampled_with_sex.extend(sampled_without_sex)

    evaluate(df, sampled_with_sex)

    if i > 30:
        remaining = df[~df['filename'].isin(sampled)]

        emotion_id_counts = remaining["emotion_id"].value_counts()

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
