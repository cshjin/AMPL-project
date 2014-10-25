
% original matrix
FigHandle = figure('Position', [50, 50, 750, 650]);
name = 'normal_matrix';
normal_matrix = load(strcat(name, '.csv'));
imagesc(normal_matrix);colormap(hot);colorbar;
xlabel('Weather Condition Index');
ylabel('Weather Condition Index');
title('Original weather transition matrix', 'FontSize', 20);

% resized original matrix
FigHandle = figure('Position', [50, 50, 750, 650]);
name = 'normal_matrix - Resized';
normal_matrix_resized = load(strcat(name,'.csv'));
imagesc(normal_matrix_resized);colormap(hot);colorbar;
xlabel('Weather Condition Index');
ylabel('Weather Condition Index');
title('Resized weather transition matrix', 'FontSize', 20);

% majority matrix
FigHandle = figure('Position', [50, 50, 750, 650]);
name = 'new_majority_matrix';
majority_matrix = load(strcat(name,'.csv'));
imagesc(majority_matrix);colormap(hot);colorbar;
xlabel('Weather Condition Index');
ylabel('Weather Condition Index');
title('Majority rule based transition matrix', 'FontSize', 20);

% diff matrix
FigHandle = figure('Position', [50, 50, 750, 650]);
diff_matrix = normal_matrix_resized - majority_matrix;
imagesc(diff_matrix);colormap(gray);colorbar;
xlabel('Weather Condition Index');
ylabel('Weather Condition Index');
title('Difference bewteen original and majority', 'FontSize', 15);


% print(1, '-dpng', strcat(name,'.png'));



eigs = eig(normal_matrix);
len = length(eigs);
sum = 0;
for i=1:50
    sum = sum -  eigs(i)* log(eigs(i));
end


% Von Neumann entropy of matrix 
sum(A(A~=0).*log(A(A~=0)));