from copy_no_rain_images_from_multiple_folders import copy_images_from_multiple_folders

source_folders = [
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\ra1_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\ra2_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\ra3_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\ra4_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\rb1_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\rb2_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_RealRain\\rb3_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\a1_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\a2_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\a3_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\a4_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\b1_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\b2_Rain',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\b3_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Testing_Synthetic\\b4_Rain',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t1_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t1_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t1_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t2_Rain_01',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t2_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t2_Rain_03',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t3_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t3_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t3_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t4_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t4_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t4_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t5_Rain_01',
    # 'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t5_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t5_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t6_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t6_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t6_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t7_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t7_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t7_Rain_03',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t7_Rain_04',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t8_Rain_01',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t8_Rain_02',
    'C:\\Users\\yanam\\opady_dataset\\SPAC-SupplementaryMaterials-master\\Dataset_Training_Synthetic\\t8_Rain_03',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Egensevej\\2-new',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Egensevej\\3-new',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Egensevej\\4-new',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Hjorringvej\\3-new',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Hobrovej\\1-new',
    # 'C:\\Users\\yanam\\opady_dataset\\archive\\aaurainsnow\\Ostre\\2-new',
    # 'C:\\Users\\yanam\\opady_dataset\\GTAV-NightRain\\set1\\test\\rainy',
    ]

destination_folder = 'C:\\Users\\yanam\\opady_dataset\\dataset\\opady_spac'

copy_images_from_multiple_folders(source_folders, destination_folder, start_index=1)