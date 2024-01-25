import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from nexa_py_sentimotion_mapper.sentimotion_mapper import Mapper
from nexa_coding_interpreter.metadata import Metadata

# TODO: Find the error files...


path = "../files/videos"

files = os.listdir(path)

metas = []

for i in files:
    filename = Path(i).stem

    meta = Metadata(filename)

    if meta.error:
        print(meta.filename)
        print(meta.intensity_level)

    if meta.intensity_level in [2, 3]:

        metas.append(vars(meta))


print(len(metas))

# df = pd.DataFrame.from_records(metas)
#
# emotion_id_counts = df["emotion_1_id"].value_counts()
#
# # Map emotion IDs to actual emotions using your Mapper class
# mapped_emotions = emotion_id_counts.index.map(Mapper.get_emotion_from_id)
#
# # Create a histogram plot
# plt.figure(figsize=(12, 6))
# plt.bar(mapped_emotions, emotion_id_counts.values)
#
# # Customize the plot
# plt.xlabel('Emotion')
# plt.ylabel('Frequency')
# plt.title('Frequency of Responses for Emotions')
# plt.xticks(rotation=90)  # Rotate x-axis labels for readability
#
# plt.tight_layout()
#
# # Show the plot
# plt.show()


# # Step 3 & 4: Group by 'video_id' and 'emotion_1_id' and count instances
# grouped_counts = df.groupby(['video_id', 'emotion_1_id']).size()
#
# # Step 5: Filter groups to find those with fewer than 4 instances
# fewer_than_four = grouped_counts[grouped_counts < 4]
#
# result = grouped_counts[grouped_counts < 4].reset_index()[['video_id', 'emotion_1_id']]
#
# # Perform an inner join to filter rows that match the video_id and emotion_1_id in 'result'
# selected_rows = pd.merge(df, result, on=['video_id', 'emotion_1_id'])
