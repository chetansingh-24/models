
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class RelevanceCalculator:
    def __init__(self):
        pass

    def compute_relevancy_score(self, candidate_data: dict, article_text: str):
        candidate_text = ' '.join(str(candidate_data.get(attr, '')) for attr in [
            'Name', 'DOB', 'Gender', 'Nationality', 'Languages_Preferred',
            'Permanent_Address', 'Religion', 'Caste_Community', 'Ethnicity',
            'Name_enrolled_as_voter_in', 'Self_profession', 'Education_level',
            'Political_Base', 'Education_Institutes_attended', 'Current_Occupation',
            'Previous_Occupation', 'Years_of_experience_in_leadership',
            'Political_party_affiliation', 'Previous_Political_positions_held',
            'Political_ideology_core_beliefs', 'Key_Areas_of_Focus',
            'Primary_Vision_for_the_Country_Region'
        ])

        candidate_embedding = model.encode(candidate_text)
        article_embedding = model.encode(article_text)
        relevancy_score = util.pytorch_cos_sim(candidate_embedding, article_embedding).item()

        return {
            "Name": candidate_data.get('Name', ''),
            "RelevancyScore": relevancy_score
        }
