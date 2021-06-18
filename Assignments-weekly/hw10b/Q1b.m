A = randn(3,3);

%symmetric matrices are nice
A = A'*A;

[Va,Da] = eigs(A);
disp('Eigenvalues of A ->');
diag(Da)
disp('Eignevectors of A ->');
Va

disp('');

B = [3*A A; zeros(3,3) 2*A];
[Vb,Db] = eigs(B);
disp('Eigenvalues of B ->');
diag(Db)
disp('Eignevectors of B ->');
Vb

