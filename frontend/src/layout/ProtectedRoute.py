def protect(auth,content): return content if auth else {'error':'unauthorized'}
