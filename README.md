# LLM CSV Sentiment Analysis
## وصف المشروع
هذا المشروع يوضح كيفية استخدام **نموذج LLM** لتحليل بيانات نصية موجودة في ملف CSV.  
المثال يحتوي على تعليقات وهمية لمنتجات/خدمات، ويتم تحليل كل تعليق لتصنيف المشاعر: إيجابي، سلبي، أو محايد.

## المحتويات
- `csv_sentiment_analysis.ipynb` : Notebook يحتوي على الكود خطوة بخطوة.
- `sample_comments.csv` : ملف CSV تجريبي يحتوي على التعليقات.

## خطوات التشغيل
1. افتح Notebook على [Google Colab](https://colab.research.google.com/).  
2. ارفع ملف `example.csv`.  
3. شغل كل الخلايا بالترتيب.  
4. في النهاية، سيتم إنشاء ملف Excel جديد يحتوي على التعليقات وتحليل المشاعر.

## النماذج المستخدمة
- `nlptown/bert-base-multilingual-uncased-sentiment` لتحليل المشاعر.

## ملاحظات
- يمكن استبدال ملف CSV بملف حقيقي من بياناتك.
- المشروع يظهر مهارتك في **Python + Pandas + Hugging Face Transformers + LLM**.
