
disp('')
n=100;
A = rand(n,n);
A=diag(diag(A)) + triu(A,1) + triu(A,1)';

%% USING ORTHOGONALISATION %%
v1=randn(n,1);
for k=1:1000
  v1=A*v1;
  v1=v1/norm(v1);
end
lambda_1 = ((A*v1)'*v1) / (v1'*v1);

%note: v1 is already unit length
v2 = randn(n,1);
v2 = (eye(n,n) - v1*v1')*v2;
for k=1:1000
  v2 = A*v2;
  v2 = (eye(n,n) - v1*v1')*v2;
  v2 = v2/norm(v2);
end
lambda_2 = ((A*v2)'*v2) / (v2'*v2);

%note: v1 and v2 are already unit length
% projection_matrix_onto_columnspace_of_A = A * inv(A'*A) * A' 
eigvecs = [v1 v2];
eigvecs_projection_matrix = eigvecs * inv(eigvecs' * eigvecs) * eigvecs';
v3 = randn(n,1);
v3 = (eye(n,n) - eigvecs_projection_matrix) * v3;
for k=1:1000
  v3 = A*v3;
  v3 = (eye(n,n) - eigvecs_projection_matrix) * v3;
  v3 = v3 / norm(v3);
end
lambda_3 = ((A*v3)'*v3) / (v3'*v3);

%% BY SUBTRACTING THE 1st and 2nd MAJOR SPECTRAL COMPONENTS

A_less_1 = A - v1 * lambda_1 * pinv(v1);
vv2 = randn(n,1);
for k=1:1000
  vv2 = A_less_1 * vv2;
  vv2 = vv2 / norm(vv2);
end
lambda_2_spectral = ((A*vv2)'*vv2) / (vv2'*vv2);

A_less_2 = A_less_1 - vv2 * lambda_2_spectral * pinv(vv2);
vv3 = randn(n,1);
for k=1:1000
  vv3 = A_less_2 * vv3;
  vv3 = vv3/norm(vv3);
end
lambda_3_spectral = ((A*vv3)'*vv3) / (vv3'*vv3);
 
disp('using orthogonalisation and power method->');
lambda_1
lambda_2
lambda_3
disp('')
disp('By subtracting spectral component ->')
disp('lambda_1_spectral == lambda_1')
lambda_2_spectral
lambda_3_spectral
disp('')
disp('using eigs funtion ->');
eigs(A,5)
 
