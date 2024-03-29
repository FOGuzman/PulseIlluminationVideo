from torch.utils.data import Dataset
import os
import torch
import scipy.io as scio

## Loader for training, uses one mat file per datapoint
class Imgdataset(Dataset):

    def __init__(self, path):
        super(Imgdataset, self).__init__()
        self.data = []
        if os.path.exists(path):
            gt_path = path

            if os.path.exists(gt_path):
                gt = os.listdir(gt_path)
                self.data = [{'orig': gt_path + '/' + gt[i]} for i in range(len(gt))]
            else:
                raise FileNotFoundError('path doesnt exist!')
        else:
            raise FileNotFoundError('path doesnt exist!')

    def __getitem__(self, index):

         data = self.data[index]["orig"]
         name = data[-10:]
         data = scio.loadmat(data)        
         meas1 = data['meas1']
         meas1 = torch.unsqueeze(torch.from_numpy(meas1),0)
         meas2 = data['meas2']
         meas2 = torch.unsqueeze(torch.from_numpy(meas2),0)        
         measc = data['measc']
         measc = torch.unsqueeze(torch.from_numpy(measc),0)

         return meas1,meas2,measc,name

    def __len__(self):

        return len(self.data)
    
class ImgdatasetRef(Dataset):

    def __init__(self, path):
        super(ImgdatasetRef, self).__init__()
        self.data = []
        if os.path.exists(path):
            gt_path = path

            if os.path.exists(gt_path):
                gt = os.listdir(gt_path)
                self.data = [{'orig': gt_path + '/' + gt[i]} for i in range(len(gt))]
            else:
                raise FileNotFoundError('path doesnt exist!')
        else:
            raise FileNotFoundError('path doesnt exist!')

    def __getitem__(self, index):

         data = self.data[index]["orig"]
         name = data[-10:]
         data = scio.loadmat(data)        
         meas1 = data['meas1']
         meas1 = torch.unsqueeze(torch.from_numpy(meas1),0)
         meas2 = data['meas2']
         meas2 = torch.unsqueeze(torch.from_numpy(meas2),0)        
         meas3 = data['meas3']
         meas3 = torch.unsqueeze(torch.from_numpy(meas3),0)

         return meas1,meas2,meas3,name

    def __len__(self):

        return len(self.data)

