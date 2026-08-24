from client import AyurvedicHolisticWellnessPersonalizedNutritionClient

def main():
    client = AyurvedicHolisticWellnessPersonalizedNutritionClient()
    res = client.formulate_ayurvedic_regimen('gut_health_and_skin_glow', 'kapha_pitta')
    print('Consultation: ' + res['consultation_id'] + ' (Dosha: ' + res['dominant_dosha'] + ')')
    print('Formulation: ' + ', '.join(res['ayurvedic_herbal_formulation']))
    print('AYUSH Certification: ' + res['ayush_certified_standard'] + ' | Efficacy: ' + str(res['clinical_efficacy_reported_pct']) + '%')

if __name__ == '__main__':
    main()
