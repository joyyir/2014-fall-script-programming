import urllib
s = urllib.urlopen('http://cse.kut.ac.kr/').read()
temp_result = []
open_cnt = 0
close_cnt = 0
is_in_par = False;
is_style_script = False;
range_s = range(len(s));
for k in range_s:
	if is_in_par:
		if s[k] == '>':
			close_cnt = close_cnt + 1
			if s.startswith('/style', k-6) or s.startswith('/STYLE', k-6) or\
			s.startswith('/script', k-7) or s.startswith('/SCRIPT', k-7) :
				is_style_script = False;
			if open_cnt == close_cnt:
				is_in_par = False
			continue
		elif s[k] == '<':
			open_cnt = open_cnt + 1
		else:
			continue
	else: # not in par
		if s[k] == '<':
			temp_result.append(' ')
			open_cnt = open_cnt + 1
			is_in_par = True
			if s.startswith('style', k+1) or s.startswith('STYLE', k+1) or\
			s.startswith('script', k+1) or s.startswith('SCRIPT', k+1) :
				is_style_script = True;
			continue
		else:
			if is_style_script:
				continue
			else:
				temp_result.append(s[k])
result = ''.join(temp_result)
print result
print
print '총 단어의 수 = ' + str(len(result.split()))
