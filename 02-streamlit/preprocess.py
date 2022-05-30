# TODO: 1. regular expression 
    # TODO: 1.1. 링크 홈페이지 - 유투브/ 신문사/ 네이버 블로그 등.
    # TODO: 1.2. 회원 분포 - 대화로는 어려울 것 같음
    # TODO: 1.3. 구분자: [닉네임/ 목표], 목표를 꺼내올 것. 
    # TODO: 1.4. 삭제된 메세지 - 
    # TODO: 1.5. 대화 시간 빈도
#%%
import pandas as pd
import numpy as np
import re

# Get pd.DataFrame
def get_df(data_path : str) -> pd.DataFrame:
    '''
        [nickname/ purpose] [time] [scripts]
    '''

    data = []

    with open(data_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == '[':
                data.append(line)
            else:
                lines[-1] = lines[-1] + line
    data = [line.split('] ') for line in data]
    
    df = pd.DataFrame(data)
    df[2] = df[2].astype(str) + df[3].astype(str) 
    df = df.drop(columns=[3])
    return df


path = '/home/sonic/workspace/ttl/Boostcamp-AI-Tech-Product-Serving/part2/02-streamlit/data/snu_kakao_real_estate.txt'
data = get_df(data_path=path)
print(data[0])


#%%
# 링크를 모두 얻어오는 함수 
def get_link(data: pd.DataFrame) -> list:

    return 


