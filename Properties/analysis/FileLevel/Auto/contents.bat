und create -db C:\SCA\analysis\FileLevel\Auto\file_contents
und add C:\SCA\analysis\FileLevel\Auto\couchdb-master -db C:\SCA\analysis\FileLevel\Auto\file_contents
und settings -GeneralFileEncoding "UTF-8" -db C:\SCA\analysis\FileLevel\Auto\file_contents
und analyze -all -db C:\SCA\analysis\FileLevel\Auto\file_contents
und settings -reportReports "File Contents" -db C:\SCA\analysis\FileLevel\Auto\file_contents
und report -db C:\SCA\analysis\FileLevel\Auto\file_contents