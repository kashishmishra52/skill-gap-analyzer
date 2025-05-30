import json

def load_resources(filepath="data/skill_resources.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def recommend_for_skills(missing_skills, resource_map):
    recommendations = {}
    for skill in missing_skills:
        if skill in resource_map:
            recommendations[skill] = resource_map[skill]
        else:
            recommendations[skill] = ["No resources available."]
    return recommendations
