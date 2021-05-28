# Bài tập Geometric
# Nhóm 12

## Trình bày giải thuật 
Có thể phát biểu lại bài toán như sau:

Kiểm tra tập đỉnh đã cho có nằm trên đa giác lồi cho trước.

- Như vậy, ta chỉ cần duyệt qua từng cạnh (2 đỉnh liền kề đa giác lồi) và kiểm tra với tất cả các đỉnh còn lại:
    - Nếu tất cả đều nằm về một phía (tiếp tục duyệt cạnh khác)
    - Nếu các đỉnh nằm ở cả 2 phía của cạnh xét -> lập tức kết thúc và báo "No"
- Sau khi duyệt hết và thỏa mãn -> kết luận đa giác đã cho là bao lồi của tập n đỉnh

## Độ phức tạp
O(mn)