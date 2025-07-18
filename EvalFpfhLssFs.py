from dataset_pc import Dataset3dad_train,Dataset3dad_test
from feature_extractors.ransac_position import get_registration_part_np,get_registration_refine_np
from feature_extractors.fpfh_pc_features import PC_FPFHFeatures
from torch.utils.data import DataLoader
import os
import numpy as np

real_3d_classes = ['airplane','car','candybar','chicken','diamond','duck','fish','gemstone','seahorse','shell','starfish','toffees']

root_dir = './data'
read_dir1 = './calculated_ADscore/fpfh_iss_fs/'
image_rocaucs_list = []
pixel_rocaucs_list = []
image_aupr_list = []
pixel_aupr_list = []

for real_class in real_3d_classes:
    test_loader = DataLoader(Dataset3dad_test(root_dir, real_class, 1024, True), num_workers=1,
                                batch_size=1, shuffle=True, drop_last=False)

    #print(f'Calculating {real_class}......')
    
    pc_pfph_whole = PC_FPFHFeatures()
    for data, mask, label, path in test_loader:
        path_list = path[0].split('/')
        target_path_tmp = os.path.join(read_dir1,real_class,path_list[-1]+'_point_level.npy')
        #print(target_path_tmp)
        pixel_preds_tmp = np.load(target_path_tmp)
        
        target_path_tmp = os.path.join(read_dir1,real_class,path_list[-1]+'_obj_level.npy')
        #print(target_path_tmp)
        image_preds_tmp = np.max(np.load(target_path_tmp))
        
        pc_pfph_whole.pixel_preds.extend(pixel_preds_tmp)
        pc_pfph_whole.image_preds.append(image_preds_tmp)
        pc_pfph_whole.image_labels.append(label)
        pc_pfph_whole.pixel_labels.extend(mask.flatten().numpy())
        
    pc_pfph_whole.calculate_metrics()
    image_rocaucs = round(pc_pfph_whole.image_rocauc, 3)
    image_aupr = round(pc_pfph_whole.image_aupr, 3)
    pixel_rocaucs = round(pc_pfph_whole.pixel_rocauc, 3)
    pixel_aupr = round(pc_pfph_whole.pixel_aupr, 3)
    
    image_rocaucs_list.append(image_rocaucs)
    image_aupr_list.append(image_aupr)
    pixel_rocaucs_list.append(pixel_rocaucs)
    pixel_aupr_list.append(pixel_aupr)
    print('Task:{}, object_auroc:{}, point_auroc:{}, object_aupr:{}, point_aupr:{}'.format
                    (real_class,image_rocaucs,pixel_rocaucs,image_aupr,pixel_aupr))
print('Summary: avg_object_auroc:{}, avg_point_auroc:{}, avg_object_aupr:{}, avg_point_aupr:{}'.format(np.mean(image_rocaucs_list),np.mean(pixel_rocaucs_list),np.mean(image_aupr_list),np.mean(pixel_aupr_list)))