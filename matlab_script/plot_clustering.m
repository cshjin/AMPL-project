% 
X = [cond, rela];

size = 12;
[idx, C] = kmeans(X, size);
figure;
cc = hsv(size);
for i=1:size
    plot(X(idx==i,1),X(idx==i,2),'.','color', cc(i, :),'MarkerSize',12);
    hold on
end
plot(C(:,1),C(:,2),'kx',...
     'MarkerSize',15,'LineWidth',3)
xlabel('Conditions');
ylabel('Means of r(t) for each condition')
% Y = [rela, cond];
% figure;
% [idx, C] = kmeans(Y, size);
% for i=1:size
%     plot(Y(idx==i,1),Y(idx==i,2),'.','color', cc(i, :),'MarkerSize',12);
%     hold on
% end
% plot(C(:,1),C(:,2),'kx',...
%      'MarkerSize',15,'LineWidth',3)
hold off