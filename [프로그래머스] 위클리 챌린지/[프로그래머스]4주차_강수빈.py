def solution(table, languages, preference):
    # 직업군별 언어 score dictionary 초기화
    job_lan_dicts = {}
    for job_score in table:
        score_dict = {"JAVA": 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0,
                      "PHP": 0}

        job_lan = job_score.split()
        job = job_lan[0]
        del job_lan[0]

        # 언어별 점수 dict에 넣어주기
        for idx, lan in enumerate(job_lan):
            score_dict[lan] = 5 - idx

        # 직군에 따라 추가해주기
        job_lan_dicts[job] = score_dict

    # 개발자 선호 언어 dict 초기화
    user_lan_pref = {}
    for idx, lan in enumerate(languages):
        user_lan_pref[lan] = preference[idx]

    # 직업군 별로 언어 점수와 개발자 선호 점수를 곱해 더한 값을 비교해 최고 직군을 return
    max_val = -1
    max_job = ""
    for job in job_lan_dicts.keys():
        lan_score = job_lan_dicts[job]
        score = 0
        for lan in user_lan_pref.keys():
            score += lan_score[lan] * user_lan_pref[lan]

        # 동일 점수가 있을 경우 알파벳 순서대로 정해주기
        if (score > max_val):
            max_val = score
            max_job = job
        elif (score == max_val):
            if max_job[0] > job[0]: max_job = job

    return max_job