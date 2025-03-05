import datetime

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_list = ["code", "date", "maximum", "remain"]
    
    if ext == "date":
        year = str(val_ext)[:4]
        month = str(val_ext)[4:6]
        day = str(val_ext)[6:]

        ext_day = datetime.datetime(int(year), int(month), int(day))
    
    for d in data:
        idx = ext_list.index(ext)
        
        if ext == "date":
            year = int(str(d[idx])[:4])
            month = int(str(d[idx])[4:6])
            day = int(str(d[idx])[6:])
            cri = datetime.datetime(year, month, day)

            if cri < ext_day:
                answer.append(d)
        else:
            if d[idx] < val_ext:
                answer.append(d)

    sort_idx = ext_list.index(sort_by)
    answer.sort(key=lambda x: x[sort_idx])

    return answer
