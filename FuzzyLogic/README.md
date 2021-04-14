#quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
#service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
#tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
Objek Anteseden / Konsekuen Baru menyimpan variabel dan keanggotaan universe

#quality.automf(3)
#service.automf(3)
Populasi fungsi keanggotaan otomatis dimungkinkan dengan .automf (3, 5, atau 7)

#tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
#tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
#tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])
Fungsi keanggotaan khusus dapat dibangun secara interaktif dengan familiar,

#rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
#rule2 = ctrl.Rule(service['average'], tip['medium'])
#rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])
Jika makanannya buruk ATAU layanannya buruk, tipnya akan rendah
Jika layanannya rata-rata, tipnya sedang
Jika makanannya bagus ATAU layanannya bagus, tipnya akan tinggi.

#tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
Sekarang setelah aturan ditentukan, buat sistem kontrol

#tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
buat ControlSystemSimulation lain saat mencoba menerapkan tipping_ctrl untuk Travis karena inputnya akan berbeda.

#tipping.input['quality'] = 6.5
#tipping.input['service'] = 9.8 
#tipping.compute()
mensimulasikan sistem kontrol dengan menentukan input dan memanggil metode komputasi. Misalkan 
menilai kualitas 6,5 dari 10 dan layanan 9,8 dari 10.

#print tipping.output['tip']
#tip.view(sim=tipping)
visualisasi tipping