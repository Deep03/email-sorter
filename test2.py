from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Initialize the tokenizer and model for NER
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

email_content = """Supercell and Chess.com are joining forces with incredible events, gameplay, 
and loot!  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 
‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 
‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 
‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 
 <https://www.chess.com/home?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website> 


 <https://www.chess.com/clash?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website> 

 Clash is Raiding Chess.‌com! 

 Chess.‌com is joining forces with Supercell to bring you a new game variant, 
features, events, and more. Explore what's new below! 

 Count Me In!  <https://www.chess.com/clash?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website> 

 <https://www.youtube.com/c/chess?utm_medium=email&utm_campaign=website&utm_source=sendgrid.com>  <https://www.twitch.tv/chess?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>  
<https://twitter.com/chesscom?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>  <https://www.facebook.com/chess?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>  
<https://www.instagram.com/wwwchesscom/?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website> 

 <https://apps.apple.com/us/app/chess.com-play-learn-chess/id329218549?mt=8&utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>  
<https://play.google.com/store/apps/details?id=com.chess&+feature=search_result&utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>
 Want to change your email preferences? Update your Notification Settings 
<https://www.chess.com/settings/notifications?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>. 
 Please do not reply to this email. Need help? Visit Chess.‌‌com Customer 
Support <http://support.chess.com/?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>. 
 This email was sent to: lekhakdeepak10@gmail.com 


Unsubscribe 
<https://tracking.chess.com/e/encryptedUnsubscribe?_r=db56590e2eee4b8283e2c7a1b93b2241&_s=f8be7ddff040483090603ec6e5031479&_t=lC-loP-52eQGo9wxsXfDyGamePI0iHbGjJ5kcVwXq4nHZ1FxrZC4YglG2dnIONmHoSss43ooekZciHW2Tnb1EaFcg8Z2hV8YcOy4P2TB9KPwG2W_cdUhcr6ohAGrMADVeqnbx_rGQDgHZFuJnUxJS5ziVJzgtv7lDldD1H2HAWA%3D&utm_source=sendgrid.com&utm_medium=email&utm_campaign=website>
 |Privacy Policy <http://www.chess.com/privacy?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website> 

 Chess‌.‌com | PO Box 970397 Orem, UT 84097 

 ©2023 

 """
ner_results = nlp(email_content)
print(ner_results)
# sensitive_words = {result['word'] for result in ner_results}
# print(sensitive_words)