# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/alfa1/PythonEditorWrapper_f23315a7-8c1b-4a2b-8182-5ee76c6abd03')
dataset = pandas.read_csv('input_df_44b9b175-aa56-4b35-9327-34f4604f9d14.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(exam_score, attendance_percentage, exercise_frequency, mental_health_rating, netflix_hours, sleep_hours, social_media_hours, study_hours_per_day)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import seaborn as sns
import matplotlib.pyplot as plt
hm = sns.heatmap(dataset.corr(), annot=True)
plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/alfa1/PythonEditorWrapper_f23315a7-8c1b-4a2b-8182-5ee76c6abd03')
