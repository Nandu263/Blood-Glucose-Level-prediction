def health_warning(status):
    if status == "Normal":
        return "✅ Healthy condition. Keep it up!"
    elif status == "Prediabetic":
        return "⚠️ May lead to Diabetes if ignored. Regular check-up needed."
    else:
        return "🚨 Severe risk! Can cause heart disease, kidney failure, vision loss."