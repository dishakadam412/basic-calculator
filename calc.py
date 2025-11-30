{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN/HHZCJl2Ti+gXha65BKFx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dishakadam412/basic-calculator/blob/main/calc.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "operator = input(\"What operation would you like to use? (+ - * /) : \")\n",
        "a = float(input(\"Enter your 1st number: \"))\n",
        "b = float(input(\"Enter your 2nd number: \"))\n",
        "\n",
        "## asks users for operation and numbers\n",
        "\n",
        "if operator == \"+\":\n",
        "  result = a+b\n",
        "  print(result)\n",
        "elif operator == \"-\":\n",
        "  result = a-b\n",
        "  print(result)\n",
        "elif operator == \"*\":\n",
        "  result = a*b\n",
        "  print(result)\n",
        "elif operator == \"/\":\n",
        "  result = a/b\n",
        "  print(result)\n",
        "\n",
        "## calculates numbers based on operator\n",
        "\n",
        "else:\n",
        "  print(f\"{operator} is not a valid operator\")\n",
        "\n",
        "## if operator is a word, it will be flagged as invalid\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "mve6FSAOM3x6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "operator = input(\"What operation would you like to use? (+ - * /) : \")\n",
        "a = float(input(\"Enter your 1st number: \"))\n",
        "b = float(input(\"Enter your 2nd number: \"))\n",
        "\n",
        "## asks users for operation and numbers\n",
        "\n",
        "if operator == \"+\":\n",
        "  result = a+b\n",
        "  print(result)\n",
        "elif operator == \"-\":\n",
        "  result = a-b\n",
        "  print(result)\n",
        "elif operator == \"*\":\n",
        "  result = a*b\n",
        "  print(result)\n",
        "elif operator == \"/\":\n",
        "  result = a/b\n",
        "  print(result)\n",
        "\n",
        "## calculates numbers based on operator\n",
        "\n",
        "else:\n",
        "  print(f\"{operator} is not a valid operator\")\n",
        "\n",
        "## if operator is a word, it will be flagged as invalid\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sw_lYkqcXr0q",
        "outputId": "1bcf9ef1-609b-487c-a587-15fce7cb97c5"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What operation would you like to use? (+ - * /) : *\n",
            "Enter your 1st number: 10\n",
            "Enter your 2nd number: 5\n",
            "50.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "operator = input(\"What operation would you like to use? (+ - * /) : \")\n",
        "a = float(input(\"Enter your 1st number: \"))\n",
        "b = float(input(\"Enter your 2nd number: \"))\n",
        "\n",
        "## asks users for operation and numbers\n",
        "\n",
        "if operator == \"+\":\n",
        "  result = a+b\n",
        "  print(result)\n",
        "elif operator == \"-\":\n",
        "  result = a-b\n",
        "  print(result)\n",
        "elif operator == \"*\":\n",
        "  result = a*b\n",
        "  print(result)\n",
        "elif operator == \"/\":\n",
        "  result = a/b\n",
        "  print(result)\n",
        "\n",
        "## calculates numbers based on operator\n",
        "\n",
        "else:\n",
        "  print(f\"{operator} is not a valid operator\")\n",
        "\n",
        "## if operator is a word, it will be flagged as invalid\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9xKTlQOeXwdm",
        "outputId": "5638c198-9651-4bf5-f3c1-4fa4f1eac0da"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What operation would you like to use? (+ - * /) : +\n",
            "Enter your 1st number: 83.3\n",
            "Enter your 2nd number: 21.3\n",
            "104.6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "operator = input(\"What operation would you like to use? (+ - * /) : \")\n",
        "a = float(input(\"Enter your 1st number: \"))\n",
        "b = float(input(\"Enter your 2nd number: \"))\n",
        "\n",
        "## asks users for operation and numbers\n",
        "\n",
        "if operator == \"+\":\n",
        "  result = a+b\n",
        "  print(result)\n",
        "elif operator == \"-\":\n",
        "  result = a-b\n",
        "  print(result)\n",
        "elif operator == \"*\":\n",
        "  result = a*b\n",
        "  print(result)\n",
        "elif operator == \"/\":\n",
        "  result = a/b\n",
        "  print(result)\n",
        "\n",
        "## calculates numbers based on operator\n",
        "\n",
        "else:\n",
        "  print(f\"{operator} is not a valid operator\")\n",
        "\n",
        "## if operator is a word, it will be flagged as invalid\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C_DgEkDiX1h5",
        "outputId": "007eecc2-8fcb-4a14-dfc6-cea15553b98a"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What operation would you like to use? (+ - * /) : /\n",
            "Enter your 1st number: 54.5\n",
            "Enter your 2nd number: 25.5\n",
            "2.1372549019607843\n"
          ]
        }
      ]
    }
  ]
}