def format(data):

    user_id = data.get('user', {}).get('id')
    username = data.get('user', {}).get('username')
    issue_title = data.get('issue', {}).get('title')
    comments = data.get('comments')
    platform = data.get('issue', {}).get('platform')
    project_platform = data.get('issue', {}).get('project', {}).get('platform') 


    output = f"""
    User ID: {user_id}
    Username: {username}
    Issue Title: {issue_title}
    Comments: {comments}
    Platform: {platform} (Project Platform: {project_platform}) 
    """
    
    return output