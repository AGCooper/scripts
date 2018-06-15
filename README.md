# scripts

cat /home/alex/Downloads/incident.csv |while read line; do echo ${line} | service_now_analysis.py; done

----
