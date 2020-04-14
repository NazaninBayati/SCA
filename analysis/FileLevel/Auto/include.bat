und create -db C:\SCA\analysis\FileLevel\Auto\include_file
und add C:\SCA\analysis\FileLevel\Auto\couchdb-master -db C:\SCA\analysis\FileLevel\Auto\include_file
und settings -GeneralFileEncoding "UTF-8" -db C:\SCA\analysis\FileLevel\Auto\include_file
und analyze -all -db C:\SCA\analysis\FileLevel\Auto\include_file
und settings -reportReports "Include File Cross Reference" -db C:\SCA\analysis\FileLevel\Auto\include_file
und report -db C:\SCA\analysis\FileLevel\Auto\include_file