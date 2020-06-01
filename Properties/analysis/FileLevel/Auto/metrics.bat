und create -db C:\SCA\analysis\FileLevel\Auto\file_Metrics
und add C:\SCA\analysis\FileLevel\Auto\couchdb-master -db C:\SCA\analysis\FileLevel\Auto\file_Metrics
und settings -GeneralFileEncoding "UTF-8" -db C:\SCA\analysis\FileLevel\Auto\file_Metrics
und analyze -all -db C:\SCA\analysis\FileLevel\Auto\file_Metrics
und settings -reportReports "File Metrics" -db C:\SCA\analysis\FileLevel\Auto\file_Metrics
und report -db C:\SCA\analysis\FileLevel\Auto\file_Metrics