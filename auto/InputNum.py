import pyautogui


def arr():
    # 从输入框获取字符串
    input_str = pyautogui.prompt('请依次输入：(素材名),(出价),(计划名字),(账户),(商品号)', '输入', )  # type: ignore

    if input_str:  # 如果用户没有取消输入
        # 使用中文逗号分割字符串
        data_list = input_str.split('，')
        # 如果需要移除每个元素的前后空格
        cleaned_list = [item.strip() for item in data_list]
        print("清理后的列表:", cleaned_list)
        return cleaned_list
