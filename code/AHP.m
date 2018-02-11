
fid = fopen('input.txt','r');
n1 = 3; n2 = 4;
a = [];
for i = 1:n1
	tmp = str2num(fgetl(fid));
	a=[a;tmp];
end
for i = 1:n1
    str1 = char(['b',int2str(i),'=[];']);
    str2 = char(['b',int2str(i),'=[b', int2str(i), ';tmp];']);
    eval(str1);
    for j = 1:n2
   		tmp = str2num(fgetl(fid));
   		eval(str2);
    end
end
ri = [0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45]; % 一致性指标
[x,y] = eig(a);
lambda = max(diag(y));
num = find(diag(y)==lambda);
w0 = x(:,num)/sum(x(:,num));
cr0 = (lambda-n1)/(n1-1)/ri(n1)
w1 = zeros(n2,n1);
for i = 1:n1
	[x,y] = eig(eval(char(['b',int2str(i)])));
    x = real(x);
    y = real(y);
	lambda = max(diag(y));
	num = find(diag(y)==lambda);
	w1(:,i) = x(:,num)./sum(x(:,num));
	cr1(i) = (lambda-n2)/(n2-1)/ri(n2);
end
cr1, ts = w1*w0 , cr = cr1*w0

