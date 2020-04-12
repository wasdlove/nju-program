import html2canvas from "html2canvas";
import jspdf from "jspdf";

export function toPdf(ele) {
  html2canvas(ele).then(canvas => {
    var contentWidth = canvas.width;
    var contentHeight = canvas.height;
    var pageHeight = (contentWidth / 592.28) * 841.89;
    var leftHeight = contentHeight;
    //页面偏移
    var position = 0;
    //a4纸的尺寸[595.28,841.89]，html页面生成的canvas在pdf中图片的宽高
    var imgWidth = 560;
    var imgHeight = (595.28 / contentWidth) * contentHeight;
    var pageData = canvas.toDataURL("image/jpeg", 1.0);
    var pdf = new jspdf("p", "pt", "a4");

    //放大会清晰一点
    pdf.internal.scaleFactor = 1.33;
    //有两个高度需要区分，一个是html页面的实际高度，和生成pdf的页面高度(841.89)
    //当内容未超过pdf一页显示的范围，无需分页
    if (leftHeight < pageHeight) {
      pdf.addImage(pageData, "JPEG", 20, 40, imgWidth, imgHeight);
    } else {
      while (leftHeight > 0) {
        pdf.addImage(pageData, "JPEG", 20, position + 40, imgWidth, imgHeight);
        leftHeight -= pageHeight;
        position -= 841.89;
        //避免添加空白页
        if (leftHeight > 0) {
          pdf.addPage();
        }
      }
    }
    pdf.save('方案配置.pdf');
  });
}
