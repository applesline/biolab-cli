# 1.创建工作流
python3 biolab.py workflow create --name "单菌分析流程" --code singlestrain --step qcstat
python3 biolab.py workflow create --name "单菌分析流程" --code singlestrain --step dataassembly --prestep "qcstat"

# 2.创建工作流算法
python3 biolab.py script create --workflowcode singlestrain --step qcstat --script docker.io/qcstat:v1.0.1
python3 biolab.py script create --workflowcode singlestrain --step dataassembly --script docker.io/dataassembly:v1.0.1

# 3.创建算法的Input模板
python3 biolab.py env create --workflowcode singlestrain --step qcstat --type Input --key read1 --feature _R1.fq.gz
python3 biolab.py env create --workflowcode singlestrain --step qcstat --type Input --key read2 --feature _R2.fq.gz
python3 biolab.py env create --workflowcode singlestrain --step qcstat --type Output --key file1 --feature qcstat.txt
python3 biolab.py env create --workflowcode singlestrain --step dataassembly --type Input --key file1 --feature qcstat.txt

# 4.注册样本地址
python3 biolab.py file create --basedir /mnt/c/Users/xxx/20241121

# 5.创建分析任务
python3 biolab.py task create --workflowcode singlestrain --step qcstat --uniqueno MN100_E112
python3 biolab.py task create --workflowcode singlestrain --step dataassembly --uniqueno MN100_E112