# 低碳飲食法 App 邏輯實作 ! (楊閔茹)
# 輸入(性別、年齡、身高(公分)、體重(公斤)、體脂率(百分比)、活動因子、壓力因子)
gender = input('請輸入性別(男/女):')
age = int(input('請輸入年齡:'))
height = float(input('身高（公分）:'))
weight = float(input('體重（公斤）:'))
fatness = float(input('體脂率（百分比）:'))
activity_factor = float(input('活動因子:'))
stress_factor = float(input('壓力因子:'))

# 計算「BMI」
BMI = weight / (height/100)**2

# 計算「BMI」狀態
if BMI<18.5:
    BMI_status = '過輕'
elif 18.5<=BMI<24:
    BMI_status = '正常'
elif 24<=BMI<27:
    BMI_status = '過重'
elif 27<=BMI<30:
    BMI_status = '輕度肥胖'
elif 30<=BMI<35:
    BMI_status = '中度肥胖'
else:
    BMI_status = '重度肥胖'

# 計算「除脂體重」
weight_without_fat = weight * (100-fatness)/100

# 計算「基礎代謝率（BMR)」、計算「總熱量消耗（TDEE）」、「低碳飲食法三大營養素的建議克數」
if gender == '男':
    BMR = 66 + ( 13.7*weight + 5*height - 6.8*age)
    TDEE = BMR*activity_factor*stress_factor
    carbohydrate = TDEE*0.2/4
    protein = TDEE*0.3/4
    fat = TDEE*0.5/9
else:
    BMR = 655 + ( 9.6*weight + 1.8*height - 4.7*age)
    TDEE = BMR*activity_factor*stress_factor
    carbohydrate = TDEE*0.2/4
    protein = TDEE*0.3/4
    fat = TDEE*0.5/9

# 輸出 
print('\n','#------您的健康飲食報告------#')
print('您的BMI為:','%.2f' %BMI)
print('您的除脂體重為:','%.2f' %weight_without_fat)
print('您的體重狀態為:',BMI_status)
print('您的體脂率為:',fatness,'%')
print('您的基礎代謝率為:','%2f' %BMR)
print('您的總熱量消耗為:','%2f' %TDEE,'\n')
print('您的低碳飲食法三大營養素建議克數為:')
print('碳水化合物:','%2f' %carbohydrate,'克')
print('蛋白質:','%.2f' %protein,'克')
print('脂肪:','%.2f' %fat,'克')