#!/bin/bash
# Назва файлу для логів
log_file="website_status.log"
# Масив URL-адрес для перевірки
websites=(
    "https://google.com"
    "https://facebook.com"
    "https://twitter.com"
)
# Очищення файлу логів перед початком
> "$log_file"
# Функція для перевірки статусу веб-сайту
check_website() {
    local url=$1
    local status_code=$(curl -sS -o /dev/null -w "%{http_code}" -L "$url")
    
    if [[ $status_code == 200 ]]; then
        echo "$url is UP"
    else
        echo "$url is DOWN"
    fi
}
# Перевірка кожного сайту
for site in "${websites[@]}"
do
    result=$(check_website "$site")
    echo "$result" >> "$log_file"
    echo "$result"
done
# Вивід повідомлення про завершення
echo -e "\nРезультати перевірки записано у файл $log_file"
