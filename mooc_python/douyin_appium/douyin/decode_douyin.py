import json
try:
    from douyin.handle_mongo import save_task,save_data
except:
    from handle_mongo import save_task,save_data

def response(flow):
    if 'aweme/v1/user/follower/list/' in flow.request.url:

        for user in json.loads(flow.response.text)['followers']:
            douyin_info = {}
            douyin_info['share_id'] = user['uid']
            douyin_info['douyin_id'] = user['short_id']
            douyin_info['nickname'] = user['nickname']
            print(douyin_info)
            save_task(douyin_info)
            # save_data(douyin_info)

