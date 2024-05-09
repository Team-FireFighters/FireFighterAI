from collections import defaultdict

class Rule:
   def __init__(self, conditions, disease):
       self.conditions = conditions
       self.disease = disease


class InferenceEngine:
   def __init__(self):
       self.rules = []
  
   def add_rule(self, conditions, disease):
       rule = Rule(conditions, disease)
       self.rules.append(rule)
  
   def predict_disease(self, symptoms):
       disease_counts = defaultdict(float)
      
       # Apply rules
       for rule in self.rules:
           matched_conditions = 0
           for condition, value in rule.conditions.items():
               if symptoms.get(condition) == value:
                   matched_conditions += 1
          
           if matched_conditions == len(rule.conditions):




               disease_counts[rule.disease] += 1
      
       # Predict disease with highest count
       predicted_disease = max(disease_counts, key=disease_counts.get)
       return predicted_disease


# Example usage
if __name__ == "__main__":
   engine = InferenceEngine()
  
   # Defining rules
   rules = [
   # Disease 1: Common Cold
   ({"high_fever": True, "cough": True}, "Common Cold"),
   ({"runny_nose": True, "sneezing": True}, "Common Cold"),
  
   # Disease 2: Influenza (Flu)
   ({"fever": True, "body_aches": True}, "Influenza (Flu)"),
   ({"sore_throat": True, "fatigue": True}, "Influenza (Flu)"),
  
   # Disease 3: Migraine
   ({"headache": True, "nausea": True}, "Migraine"),
   ({"sensitivity_to_light": True, "sensitivity_to_sound": True}, "Migraine"),
  
   # Disease 4: Pneumonia
   ({"cough": True, "shortness_of_breath": True}, "Pneumonia"),
   ({"fever": True, "chest_pain": True}, "Pneumonia"),
  
   # Disease 5: Gastroenteritis (Stomach Flu)
   ({"abdominal_pain": True, "diarrhea": True}, "Gastroenteritis (Stomach Flu)"),
   ({"nausea": True, "vomiting": True}, "Gastroenteritis (Stomach Flu)"),
  
   # Disease 6: Asthma
   ({"shortness_of_breath": True, "wheezing": True}, "Asthma"),
   ({"chest_tightness": True, "cough": True}, "Asthma"),
  
   # Disease 7: Urinary Tract Infection (UTI)
   ({"painful_urination": True, "frequent_urination": True}, "Urinary Tract Infection (UTI)"),
   ({"abdominal_pain": True, "fever": True}, "Urinary Tract Infection (UTI)"),
  
   # Disease 8: Sinusitis
   ({"facial_pain": True, "nasal_congestion": True}, "Sinusitis"),
   ({"postnasal_drip": True, "headache": True}, "Sinusitis"),
  
   # Disease 9: Streptococcal Pharyngitis (Strep Throat)
   ({"sore_throat": True, "swollen_lymph_nodes": True}, "Streptococcal Pharyngitis (Strep Throat)"),
  ({"fever": True, "difficulty_swallowing": True}, "Streptococcal Pharyngitis (Strep Throat)"),
  
   # Disease 10: Gastroesophageal Reflux Disease (GERD)
   ({"heartburn": True, "acid_reflux": True}, "Gastroesophageal Reflux Disease (GERD)"),
   ({"regurgitation": True, "difficulty_swallowing": True}, "Gastroesophageal Reflux Disease (GERD)")
]


for conditions, disease in rules:
   engine.add_rule(conditions, disease)


# Provide symptoms
symptoms = {"shortness_of_breath": True, "wheezing": True}




# Predict disease
predicted_disease = engine.predict_disease(symptoms)
print("Predicted Disease:", predicted_disease)