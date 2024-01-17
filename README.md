# Projekts "Mašīnu izvele"
## Projekta aprakts
### Situacijas apraksts
  1. Vispirms, lai uzsakt stradāt, man bija jāformulēt darbas tēmu. Darba gaitā es pieņemu lēmumu mainīt tēmu un galīgs darba nosaukums ir "Mašīnu izvele". Uz so tēmu man iedvesmoja mana draudzene, kura drīz iegūs autovadītāja apliecību un viņa grib nopirk sev auto, bet nezina kā to izdarīt un paprasija mani palīdzēt.
  2. Otrkart, man bija jāuzdod viņai  jautajumus lai saprasts kādu tiešu mašīnu viņa grib un var nopirkt. Viņa konreti izstastīja kadu marku grib un viņas budžets. Un pastastīja, ka viņa negriba uzreiz pirkt, bet pati apskatīt variantus meneša laikā.
  3. Treškart, man bija paši uzzināt kur, un kādā  veida internetā ir sludinajumi lai nopirkt mašīnu, ka arī darbojas saite.
  4. Izveidot kodu  (Visual Studio Code)
## Python bibliotēkas

Savā projektā es izmantoju tikai Selenium bibliotēku, jo tā var izmantot pārlūkprogrammās - Chrome, Firefox, Opera un citās.Lai to izmantot, vispirms bija to uzintalet. ![image](https://github.com/anastasijaskogoreva/project/assets/144266164/d04c229f-e55c-4f2f-83a1-e523fc947967)
 Lai uzzinat kā izmantot biblioteku, es paskatijos video, kas bija ierakstīt 5.lekcijas  laikā (https://www.youtube.com/watch?v=t0PBBPuPgaw), ka arī internet resursi (https://selenium-python.readthedocs.io/).
 
 ## Programmatūras izmantošanas metodes apraksts

 ### Galīgs rezultāts izskatas šādi:![image](https://github.com/anastasijaskogoreva/project/assets/144266164/8e703e83-059a-4111-a68f-42c34a0841c7)

Ja uzsakt kodu, tad atverās Chrome un ieladēs saite ar sludinajumiem un lietotājs var izvelēt sav auto jau ar gataviem datiem un katra reize augšā jau būs jaunie sludiajumi. Ta var izdarīt netikai mašīnu izvele gadijumā, net piemēram dzivokli un tt.
Ja kad pēc tam draudzene grib mainīt mašinas marku, tad ar funkciju ***inspect*** var atrast _id_, vai _class_  un mainīt to 16.rindā (find=driver.find_element(By.ID, "ahc_166") un to arī var izdarīt ar summu 24.(find.send_keys("1000")) un 26. rindās(find.send_keys("9000")).
 



   
